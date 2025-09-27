import sys
import subprocess

DEVICE_1 = "alsa_output.pci-0000_01_00.1.hdmi-stereo"
DEVICE_2 = "alsa_output.pci-0000_00_1f.3.analog-stereo"
SINK_1 = "First"
SINK_2 = "Second"

def manage_links(source, sink, unlink=False):
    action = ['-d'] if unlink else []
    subprocess.run(['pw-link', *action, f"{source}:monitor_FL", f"{sink}:playback_FL"], check=False)
    subprocess.run(['pw-link', *action, f"{source}:monitor_FR", f"{sink}:playback_FR"], check=False)
    action_str = "Unlinked" if unlink else "Linked"
    print(f"{action_str} {source} <-> {sink}")

def check_if_linked(source_port, sink_port, linked_ports_output):
    current_source = ""
    for line in linked_ports_output:
        if not line.startswith((' ', '\t')):
            current_source = line.strip()
        elif current_source == source_port and sink_port in line:
            return True
    return False

def main():
    try:
        result = subprocess.run(['pw-link', '-l'], capture_output=True, text=True, check=True)
        current_links = result.stdout.strip().split('\n')
        is_default_linked = check_if_linked(
            source_port=f"{SINK_1}:monitor_FR",
            sink_port=f"{DEVICE_1}:playback_FR",
            linked_ports_output=current_links
        )
        if is_default_linked:
            print("Default links found. Swapping to alternate.")
            manage_links(SINK_1, DEVICE_1, unlink=True)
            manage_links(SINK_2, DEVICE_2, unlink=True)
            manage_links(SINK_1, DEVICE_2)
            manage_links(SINK_2, DEVICE_1)
        else:
            manage_links(SINK_1, DEVICE_2, unlink=True)
            manage_links(SINK_2, DEVICE_1, unlink=True)
            manage_links(SINK_1, DEVICE_1)
            manage_links(SINK_2, DEVICE_2)

    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()