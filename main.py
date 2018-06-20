import player

sorcerer = player.Sorcerer(hit_points=40,mana=80)
print("El sorcerer tiene: ")
print(sorcerer.hit_points)
print(sorcerer.mana)
print(sorcerer.vocation)
print(sorcerer.cast_spell())
print(sorcerer.movement_speed)

knight = player.Knight(hit_points=80,mana=20)
print("El Knight tiene: ")
print(knight.hit_points)
print(knight.mana)
print(knight.vocation)
print(knight.cast_spell())
print(knight.movement_speed)
