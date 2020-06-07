package main

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
