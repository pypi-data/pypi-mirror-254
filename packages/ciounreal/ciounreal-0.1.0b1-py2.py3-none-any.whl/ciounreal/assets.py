import json
import os
import re
import glob

import unreal


def _find_deps(asset_path, opts, registry, deps, depth=0):
    dependencies = registry.get_dependencies(asset_path, opts)
    for dep in [str(d) for d in dependencies]:
        if dep not in deps:
            deps.add(dep)
            _find_deps(dep, opts, registry, deps, depth + 1)


def _get_dependency_options():
    options = unreal.AssetRegistryDependencyOptions()
    options.include_hard_management_references = True
    options.include_hard_package_references = True
    options.include_searchable_names = True
    options.include_soft_management_references = True
    options.include_soft_package_references = True
    return options


def _dependency_scan(root_asset):
    asset = str(root_asset)
    if not asset:
        return "[]"

    helper = unreal.AssetRegistryHelpers
    registry = helper.get_asset_registry()
    options = _get_dependency_options()

    deps = set()
    deps.add(asset)
    _find_deps(root_asset, options, registry, deps)

    result = []
    project_path = unreal.Paths.get_project_file_path()
    for i, dep in enumerate(deps):
        if not dep.startswith("/Game"):
            continue

        syspath = unreal.PackageTools.package_name_to_filename(dep)
        syspath = os.path.join(project_path, syspath)
        syspath = unreal.Paths.convert_relative_path_to_full(syspath)
        matching_paths = glob.glob(str(syspath) + ".*")
        for p in matching_paths:
            p = p.replace("\\", "/")
            result.append({"path": p, "dep": dep})
    return result


def main(root_asset, extra_assets):
    result = []
    root_asset = str(root_asset)
    try:
        result.extend(_dependency_scan(root_asset))

        extra_assets = json.loads(extra_assets)
        extra_assets = [{"path": a} for a in extra_assets]
        result.extend(extra_assets)

        return json.dumps(result)
    except BaseException as e:
        unreal.log_error("Error: " + str(e))
        return "[]"


def stat(asset_paths_json):
    asset_paths = [a["path"] for a in json.loads(asset_paths_json)]
    bytes = 0
    for asset_path in asset_paths:
        if os.path.exists(asset_path):
            if os.path.isdir(asset_path):
                bytes += _get_dir_size(asset_path)
            elif os.path.isfile(asset_path):
                bytes += os.path.getsize(asset_path)

    readable = _get_readable_size(bytes)
    return readable


def _get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += _get_dir_size(entry.path)
    return total


def _get_readable_size(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1000.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1000.0
    return f"{num:.1f}Yi{suffix}"
