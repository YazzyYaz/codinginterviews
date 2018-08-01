package main

func clearBit(num, item uint) uint {
	max := ^(1 << item)
	return num & max
}
