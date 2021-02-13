package main

// From https://github.com/faiface/beep/wiki/Composing-and-controlling

import (
	"log"
	"os"
	"time"

	"github.com/faiface/beep/speaker"
	"github.com/faiface/beep/wav"
)

func main() {
	f, err := os.Open("garuda_bowl.wav")
	if err != nil {
		log.Fatal(err)
	}
	streamer, format, err := wav.Decode(f)
	if err != nil {
		log.Fatal(err)
	}
	defer streamer.Close()

	speaker.Init(format.SampleRate, format.SampleRate.N(time.Second/10))

	speaker.Play(streamer)
	select {}
}
