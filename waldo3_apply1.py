import os

# 설정 변수들
model_path = "WALDO30_yolov8m_640x640.pt"  # 모델 경로
input_video_path = "C:\\Users\\dromii\\20240401-송도\\M3C\\120m\\DJI_0073.MP4"  # 입력 영상 경로
output_video_path = os.path.join(os.path.dirname(input_video_path), "output_sliced_inference.mp4")  # 출력 영상 경로
slice_height = 640  # 슬라이스 높이
slice_width = 640  # 슬라이스 너비
overlap_height_ratio = 0.2  # 높이 중첩 비율
overlap_width_ratio = 0.2  # 너비 중첩 비율

# 명령 실행
os.system(f"python run_sliced_inference.py {model_path} {input_video_path} {output_video_path} {slice_height} {slice_width} {overlap_height_ratio} {overlap_width_ratio}")
