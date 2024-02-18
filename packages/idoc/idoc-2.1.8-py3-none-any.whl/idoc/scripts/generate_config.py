import os.path
HOME=os.environ["HOME"]
DEFAULT_PATH=os.path.join(HOME, ".config", "idoc", "idoc.yaml")

def generate_config(path=DEFAULT_PATH):

    config=f"""
controller:
  arduino_port: /dev/ttyACM0
  mapping_path: {HOME}/.config/idoc/mega.csv
  paradigm_path: warm_up.csv
  pwm: {{}}
core:
  debug: true
default_class:
  board: ArduinoMegaBoard
  camera: PylonCamera
  drawer: DefaultDrawer
  result_writer: CSVResultWriter
  roi_builder: IDOCROIBuilder
  tracker: AdaptiveBGModel
drawer:
  kwargs:
    draw_frames: false
    framerate: null
    video_out_fourcc: DIVX
  last_annot_path: /tmp/last_img_annot.png
  last_drawn_path: /tmp/last_img.png
experiment:
  adaptation_time: 5
  location: null
  max_duration: 18000
folders:
  paradigms:
    description: Where csv files containing hardware programs are stored.
    path: {HOME}/.config/idoc/paradigms
  results:
    description: Where data will be saved by the saver class.
    path: {HOME}/idoc_data/results_temp
io:
  camera:
    args: []
    kwargs:
      drop_each: 1
      rotation: -90
      use_wall_clock: true
      video_path: None
    framerate: 5
    exposure_time: 50000
  result_writer:
    args: []
    kwargs:
      max_n_rows_to_insert: 1
network:
  port: 9000
roi_builder:
  args: []
  kwargs: {{}}
  target_coord_file: None
logging: {HOME}/.config/idoc/logging.yaml
    """

    folder=os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)

    with open(path, "w") as handle:
        handle.write(config)
