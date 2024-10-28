import pytest
import freezegun
from pymagotchi import pet, names

# Write unit tests here to test all types of valid and valid function inputs
# Marking scheme says at least 3 tests
# Order of functions to test (Some rely on others working):
# 1) pet.time_elapsed
# 2) names.generate_name
# 3) pet.__init__
# 4) pet.new_pet
# 5) pet.update_stats
# 6) pet.status
