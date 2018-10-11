name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
def make_dict(name,favoriote_animal):
	new_dict = {}
	new_dict = zip(name,favorite_animal)
	return new_dict
make_dict()