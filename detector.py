from ultralytics import YOLO

model = YOLO("yolo11n.pt")


def get_position(x_center, image_width):
    if x_center < image_width / 3:
        return "left"
    elif x_center < (2 * image_width / 3):
        return "center"
    else:
        return "right"


def detect_objects(image):

    results = model(image)
    detections = []

    result = results[0]
    image_width = image.width

    for box in result.boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        object_name = model.names[class_id]

        x1, y1, x2, y2 = box.xyxy[0].tolist()

        x_center = (x1 + x2) / 2

        position = get_position(
            x_center,
            image_width
        )

        detections.append({
            "object": object_name,
            "confidence": confidence,
            "position": position
        })

    return results, detections