package main

func repeatedShift(x, count int) int {
	for i := 0; i < count; i++ {
		x >> 1
	}
	return x
}
