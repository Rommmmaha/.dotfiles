import sys
import json
import subprocess

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <volume>", file=sys.stderr)
    sys.exit(1)
volume = sys.argv[1]
devices_to_find = {
    "GP107GL High Definition Audio Controller Digital Stereo (HDMI)",
    "Built-in Audio Analog Stereo",
}
found_device_ids = []
try:
    result = subprocess.run(["pw-dump"], capture_output=True, text=True, check=True)
    nodes = json.loads(result.stdout)
    for node in nodes:
        props = node.get("info", {}).get("props", {})
        if props.get("media.class") == "Audio/Sink":
            description = props.get("node.description", "")
            if description in devices_to_find:
                found_device_ids.append(str(node["id"]))
                if len(found_device_ids) == len(devices_to_find):
                    break
    if not found_device_ids:
        print("Could not find any of the specified audio sinks.", file=sys.stderr)
        sys.exit(1)
    for device_id in found_device_ids:
        subprocess.run(["wpctl", "set-volume", device_id, volume], check=True)
        print(f"Volume for device {device_id} set to {volume}")
except (FileNotFoundError, subprocess.CalledProcessError, json.JSONDecodeError) as e:
    print(f"An error occurred: {e}", file=sys.stderr)
    sys.exit(1)
