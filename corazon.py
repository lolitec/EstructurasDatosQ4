def main():
	letra = input()
	corazon = [
		"   FFFFFF      FFFFF   ",
		"  FFFFFFFF    FFFFFFF  ",
		" FFFFFFFFFF  FFFFFFFFF ",
		"FFFFFFFFFFFFFFFFFFFFFFF",
		"FFFFFFFFFFFFFFFFFFFFFFF",
		" FFFFFFFFFFFFFFFFFFFFF ",
		"  FFFFFFFFFFFFFFFFFFF  ",
		"   FFFFFFFFFFFFFFFFF   ",
		"    FFFFFFFFFFFFFFF    ",
		"     FFFFFFFFFFFFF     ",
		"      FFFFFFFFFFF      ",
		"       FFFFFFFFF       ",
		"        FFFFFFF        ",
		"         FFFFF         ",
		"          FFF          ",
		"           F           "
	]
	for i in corazon:
		print(i.replace("F",letra))

if __name__ == "__main__":
	main()

