# Copyright Epic Games, Inc. All Rights Reserved.
import unreal


@unreal.uclass()
class ConductorExecutor(unreal.MoviePipelinePythonHostExecutor):
    pipeline = unreal.uproperty(unreal.MoviePipeline)
    output_resolution = unreal.IntPoint

    def _post_init(self):
        self.pipeline = None
        self.seq_path = None
        self.out_directory = None
        self.output_resolution = None
        self.start_frame = None
        self.end_frame = None
        self.step_frame = None
        self.file_name_format = None

    @unreal.ufunction(override=True)
    def execute_delayed(self, inPipelineQueue):
        for x in range(0, 5):
            unreal.log_error("X" * 50)

        success = self._parse_args()
        if not success:
            self.on_executor_errored()
            return

        queue = unreal.new_object(unreal.MoviePipelineQueue, outer=self)

        job = queue.allocate_new_job(unreal.MoviePipelineExecutorJob)
        
        job.sequence = unreal.SoftObjectPath(self.seq_path)

        # Now we can configure the job.
        outputSetting = job.get_configuration().find_or_add_setting_by_class(
            unreal.MoviePipelineOutputSetting
        )

        outputSetting.use_custom_playback_range = True
        outputSetting.custom_start_frame = self.start_frame
        outputSetting.custom_end_frame = self.end_frame + 1  # +1 because it's exclusive
        outputSetting.output_frame_step = self.step_frame

        outputSetting.set_editor_property(
            "output_directory", unreal.DirectoryPath(self.out_directory)
        )

        outputSetting.output_resolution = self.output_resolution

        outputSetting.file_name_format = self.file_name_format

        # Ensure there is something to render
        job.get_configuration().find_or_add_setting_by_class(
            unreal.MoviePipelineDeferredPassBase
        )
        # Ensure there's a file output.
        job.get_configuration().find_or_add_setting_by_class(
            unreal.MoviePipelineImageSequenceOutput_PNG
        )

        # Ensure default values kick in.
        job.get_configuration().initialize_transient_settings()

        # Create movie render pipeline to run the job.
        self.pipeline = unreal.new_object(
            self.target_pipeline_class,
            outer=self.get_last_loaded_world(),
            base_type=unreal.MoviePipeline,
        )

        # Register callbacks
        self.pipeline.on_movie_pipeline_finished_delegate.add_function_unique(
            self, "on_movie_pipeline_finished"
        )

        self.pipeline.initialize(job)

    # This function is called every frame and can be used to do simple countdowns, checks
    # for more work, etc.
    @unreal.ufunction(override=True)
    def on_begin_frame(self):
        # It is important that we call the super so that async socket messages get processed.
        super(ConductorExecutor, self).on_begin_frame()
        
        if self.pipeline:
            unreal.log(
                "Progress: %f"
                % unreal.MoviePipelineLibrary.get_completion_percentage(self.pipeline)
            )

    @unreal.ufunction(override=True)
    def on_map_load(self, inWorld):
        pass

    # Don't delete this function.
    @unreal.ufunction(override=True)
    def is_rendering(self):
        return False

    @unreal.ufunction(ret=None, params=[unreal.MoviePipeline, bool])
    def on_movie_pipeline_finished(self, inMoviePipeline, bSuccess):
        """Terminate the pipeline"""
        unreal.log("Finished rendering! Success: " + str(bSuccess))
        self.pipeline = None
        self.on_executor_finished_impl()

    def _parse_args(self):
        """
        Parse commandline arguments
        Required:
            Map
            LevelSequence
            MoviePipelineConfig
            StartFrame
            EndFrame
            StepFrame

        """
        (
            cmd_tokens,
            cmd_switches,
            cmd_parameters,
        ) = unreal.SystemLibrary.parse_command_line(
            unreal.SystemLibrary.get_command_line()
        )
        success = True
        # self.map_path = cmd_tokens[0]
        unreal.log("Parsing command line arguments...")
        # LevelSequence
        self.seq_path = cmd_parameters.get("LevelSequence")
        if not self.seq_path:
            unreal.log_error("Missing argument: '-LevelSequence=/Game/MySequence'")
            success = False
        unreal.log("Parsed LevelSequence: " + self.seq_path)
        
        self.out_directory = cmd_parameters.get("OutputDirectory")
        if not self.out_directory:
            unreal.log_error(
                "Missing argument: '-OutputDirectory=/Path/to/Saved/MovieRenders'"
            )
            success = False
        unreal.log("Parsed OutputDirectory: " + self.out_directory)
        
        self.file_name_format = cmd_parameters.get("FileNameFormat")
        if not self.file_name_format:
            unreal.log_error("Missing argument: '-FileNameFormat=Something.something'")
            success = False
        unreal.log("Parsed FileNameFormat: " + self.file_name_format)
        
        res = cmd_parameters.get("OutputResolution")
        if not res:
            unreal.log_error("Missing argument: '-OutputResolution=1920x1080'")
            success = False
        res = res.split("x")
        self.output_resolution = unreal.IntPoint(int(res[0]), int(res[1]))
        unreal.log("Parsed OutputResolution: " + str(self.output_resolution))
        
        self.end_frame = int(cmd_parameters.get("EndFrame"))
        if not self.end_frame:
            unreal.log_error("Missing argument: '-EndFrame=100'")
            success = False
        unreal.log("Parsed EndFrame: " + str(self.end_frame))
        
        self.start_frame = int(cmd_parameters.get("StartFrame"))
        if not self.start_frame:
            unreal.log_error("Missing argument: '-StartFrame=1'")
            success = False
        unreal.log("Parsed StartFrame: " + str(self.start_frame))
            
        self.step_frame = int(cmd_parameters.get("StepFrame", 1))
        unreal.log("Parsed StepFrame: " + str(self.step_frame))
        
        return success
