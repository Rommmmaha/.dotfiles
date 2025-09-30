import subprocess
import json
import time


def get_open_window_classes():
    try:
        result = subprocess.run(
            ["hyprctl", "clients", "-j"], capture_output=True, text=True, check=True
        )
        clients = json.loads(result.stdout)
        return {client["class"] for client in clients if client["class"]}
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"Error getting window classes: {e}")
        return set()


def main():
    subprocess.run(["hyprctl", "dispatch", "workspace", "2"], check=True)
    rules = [
        {"classes": ["Vivaldi-stable", "vivaldi-snapshot"], "workspace": 3},
        {"classes": ["org.telegram.desktop", "org.ayugram.desktop"], "workspace": 1},
        {"classes": ["legcord"], "workspace": 1},
        {"classes": ["com.obsproject.Studio"], "workspace": 10},
        {"classes": ["kitty"], "workspace": 10},
        {
            "classes": ["com.saivert.pwvucontrol", "org.pulseaudio.pavucontrol"],
            "workspace": 10,
        },
    ]
    while True:
        open_windows = get_open_window_classes()
        all_windows_present = True
        for rule in rules:
            if not any(cls in open_windows for cls in rule["classes"]):
                all_windows_present = False
                print(
                    f"Waiting for window with one of the classes: {', '.join(rule['classes'])}"
                )
                break
        if all_windows_present:
            batch_commands = []
            for rule in rules:
                for window_class in rule["classes"]:
                    if window_class in open_windows:
                        command = f"dispatch movetoworkspacesilent {rule['workspace']},class:^({window_class})$"
                        batch_commands.append(command)
                        break
            if batch_commands:
                full_command = ["hyprctl", "--batch", ";".join(batch_commands)]
                subprocess.run(full_command, check=True)
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
