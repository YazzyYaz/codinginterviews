package main

int value

func updateBit(num, item int, bitIs1 bool) int {
    if bitIs1 == true {
	value = 1
    } else {
	value = 0
    }
    mask := ^(1 << item)
    return (num & mask) | (value << i)
}
