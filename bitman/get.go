package main

func getBit(num, item int) bool {
	return ((num & (1 << item)) != 0)
}
