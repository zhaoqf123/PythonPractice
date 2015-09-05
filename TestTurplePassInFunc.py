def test(*tpl, ele1):
	print tpl
#	print ele1
#	print ele2

tpl = ("a", "b")
test(*tpl, "c")