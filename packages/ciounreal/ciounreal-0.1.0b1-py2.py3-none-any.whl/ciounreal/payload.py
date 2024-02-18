import json
import os
import re
import unreal

from ciocore import data as coredata
from ciocore.package_environment import PackageEnvironment
from cioseq.sequence import Sequence


# level_name => Minimal_Default1
# sequence_name => CameraMove001
# job_name => CameraMove001
# frame_rate => 30.0
# date => 2023.04.16
# time => 00.35.02
# year => 2023
# month => 04
# day => 16
# version => v00x
# job_author => julia

#### Leave these
# frame_number => 0000
# frame_number_shot => 0000
# frame_number_rel => 0000
# frame_number_shot_rel => 0000


# camera_name => CameraName
# shot_name => ShotName
# render_pass => RenderPassName
# project_dir => C:/Users/julia/Documents/Unreal Projects/MRQCommandLine/
# output_resolution => 1920_1080
# output_width => 1920
# output_height => 1080


## Token generation.
def _level_name():
    les = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    return les.get_current_level().get_package().get_name().split("/")[-1]


class Context(dict):
    def __missing__(self, key):
        return key.join("{}")


def main(*args):
    payload = _resolve(*args)
    return "\n" + json.dumps(payload, indent=4)


# private
def _resolve(*args):
    """Return the submission payload"""

    (
        title,
        project,
        instance_type,
        preemptible,
        frame_spec,
        chunk_size,
        scout_spec,
        task_template,
        project_path,
        job_name,
        level_sequence,
        map_path,
        output_path,
        filename_format,
        resolution,
        use_daemon,
        location,
        notifications,
        asset_paths,
        extra_environment,
    ) = args

    title = str(title)
    scout_spec = str(scout_spec)
    frame_spec = str(frame_spec)
    task_template = str(task_template)
    job_name = str(job_name)
    level_sequence = str(level_sequence)
    map_path = str(map_path)
    output_path = str(output_path)
    filename_format = str(filename_format)
    location = str(location)
    notifications = str(notifications)
    resolution = str(resolution)

    project_dir = os.path.dirname(project_path)

    context = Context(
        {
            "project_path": project_path,
            "project_dir": project_dir,
            "job_name": job_name,
            "level_sequence": level_sequence,
            "level_sequence_name": level_sequence.split("/")[-1],
            "sequence_name": level_sequence.split("/")[-1],
            "map_path": map_path,
            "map_name": map_path.split("/")[-1],
            "level_name": _level_name(),
            "resolution": resolution,
        }
    )

    output_path = output_path.format_map(context).replace("\\", "/").rstrip("/")
    filename_format = filename_format.format_map(context).replace("\\", "/")

    context.update({"output_dir": output_path, "filename_format": filename_format})

    result = {}
    result.update(_resolve_instance_type(instance_type, preemptible))
    result.update(_resolve_project(project))
    result.update(_resolve_title(title, **context))
    result.update(_resolve_package(extra_environment))
    result.update(_resolve_output(output_path))
    result.update(_resolve_location(location))
    result.update(_resolve_notifications(notifications))
    result.update(_resolve_daemon(use_daemon))
    result.update(_resolve_assets(asset_paths, project_path, output_path))

    main_sequence, scout_sequence = _get_sequences(frame_spec, scout_spec, chunk_size)
    tasks_data = _resolve_tasks(main_sequence, scout_sequence, task_template, **context)
    result.update(tasks_data)

    return result


def _get_sequences(frame_spec, scout_spec, chunk_size):
    main_sequence = Sequence.create(
        frame_spec, chunk_size=chunk_size, chunk_strategy="progressions"
    )

    match = re.compile(r"^auto[, :]+(\d+)$").match(scout_spec)
    if match:
        num_samples = int(match.group(1))
        scout_sequence = main_sequence.subsample(num_samples)
    else:
        try:
            scout_sequence = Sequence.create(scout_spec)
        except (ValueError, TypeError):
            scout_sequence = None
    return main_sequence, scout_sequence


def _resolve_instance_type(instance_type_description, preemptible):
    hardware = coredata.data().get("instance_types")

    instance_type = hardware.find_first(
        lambda t: t["description"] == instance_type_description
        and t["operating_system"] == "windows"
        and t.get("gpu")
    )

    return {"instance_type": instance_type, "preemptible": preemptible}


def _resolve_project(project):
    return {"project": project}


def _resolve_title(title_template, **context):
    return {"job_title": title_template.format_map(context)}


# Just get the last package (it's the only one)
def _resolve_package(extra_environment):
    tree_data = coredata.data()["software"]
    last_host_name = tree_data.supported_host_names()[-1]
    last_pkg = tree_data.find_by_name(last_host_name)
    package_env = PackageEnvironment(last_pkg)
    package_env.extend(json.loads(extra_environment))

    result = {
        "software_package_ids": [last_pkg["package_id"]],
        "environment": dict(package_env),
    }
    return result


def _resolve_output(output_path, **context):
    return {"output_path": output_path.format(**context)}


def _resolve_location(location):
    location = location.strip()
    return {"location": location} if location else {}


def _resolve_notifications(notifications):
    if notifications:
        notifications = [a for a in re.split(r"[, ]+", notifications) if a and "@" in a]
        if notifications:
            return {"notify": {"emails": notifications}}
    return {}


def _resolve_daemon(use_daemon):
    return {"local_upload": not use_daemon}


def _resolve_tasks(main_sequence, scout_sequence, task_template, **context):
    """
    Task template makes use of tokens that are replaced with actual values on submission.

    Static tokens are:
    project_path: Path to the project file, automatically generated at submission time.
    level_sequence: Value of the Level Sequence field.
    map_path: Value of the map_path field.

    Chunk varying tokens are:
    start: Start frame of the current chunk.
    end: End frame of the current chunk.
    step: Step frame of the current chunk.


    """
    tasks = []
    chunks = main_sequence.chunks()

    # Test the template
    if chunks:
        test_context = Context({"start": 1, "end": 1, "step": 1})
        test_context.update(context)
        task_template.format_map(test_context)

    for chunk in chunks:
        chunk_context = Context(
            {"start": str(chunk.start), "end": str(chunk.end), "step": str(chunk.step)}
        )
        chunk_context.update(context)

        tasks.append(
            {"command": task_template.format_map(chunk_context), "frames": str(chunk)}
        )

    return {
        "scout_frames": ",".join([str(s) for s in scout_sequence or []]),
        "tasks_data": tasks,
    }


def _resolve_assets(asset_paths_json, project_path, output_path):
    """
    Create the assets definition.

    Returns an object containing assets to be merged into the submission.
    """
    asset_paths = [a["path"] for a in json.loads(asset_paths_json)]
    all_assets = [project_path]
    all_assets.extend(list(asset_paths))

    all_assets = [
        re.sub("/+", "/", a)
        for a in all_assets
        if not (a.startswith(output_path) or output_path.startswith(a))
    ]

    return {"upload_paths": list(all_assets)}
