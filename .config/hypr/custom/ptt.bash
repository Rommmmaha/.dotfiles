if [ -z "$1" ]; then
  echo "Usage: $0 [0|1]"
fi

if [ "$1" -eq 1 ]; then
  wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.4
  echo "rect 0 0 1919 1079 0xFFFFFFFF 1" | ncat -u 127.0.0.1 7435
elif [ "$1" -eq 0 ]; then
  wpctl set-volume @DEFAULT_AUDIO_SOURCE@ 0.0
  echo "rect 0 0 1919 1079 0x00000000 1" | ncat -u 127.0.0.1 7435
fi