package main

import(
	"fmt"
)

func Merge2Channels(f func(int) int, in1 <-chan int, in2 <-chan int, out chan<- int, n int) {
	go func() {
		buff := make(chan int, 2)
		for i := 0; i < n; i++ {
			x1, x2 := <-in1, <-in2
			go func() { buff <- f(x1) }()
			go func() { buff <- f(x2) }()
			out <- <-buff + <-buff
		}
	}()
}


func main() {
	n := 2
	in1 := make(chan int, n)
	in2 := make(chan int, n)
	out := make(chan int, n)
	summer := func(x int) int { return x * x }

	Merge2Channels(summer, in1, in2, out, n)
	in1 <- 1
	in2 <- 2

	in1 <- 2
	in2 <- 4

	//in1 <- 3
	//in2 <- 6

	//in1 <- 4
	//in2 <- 7

	fmt.Println(<-out)
	fmt.Println(<-out)
	//fmt.Println(<-out)
}
