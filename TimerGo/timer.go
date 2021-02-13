///usr/bin/true; exec /usr/bin/env go run "$0" "$argv(1)"
//
package main

import (
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"time"
)

func play() {
	cmd := exec.Command("./play")
	if err := cmd.Run(); err != nil {
		fmt.Println(err)
	}
}

func main() {

	fmt.Println("Usage: Run with './timer' for default 5 minute rounds. Run with './timer #' with # being the number of minutes you want per round.")

	var dur string = "5"
	if len(os.Args) == 2 {
		dur = os.Args[1]
	}
	duration, err := strconv.Atoi(dur)
	if err != nil {
		duration = 5
	}

	round := duration * 60
	roundCount := 1

	go play()

	for current := 0; current < round; current++ {
		minutes := current / 60
		seconds := current % 60

		fmt.Printf("\rRound: %v 🔔 %02v:%02v", roundCount, minutes, seconds)
		time.Sleep(1000 * time.Millisecond)
		if current == round-1 {
			current = 0
			roundCount++
			go play()
		}
	}

	fmt.Printf("%v %T", duration, duration)

}
