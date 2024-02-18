from pathlib import Path
import pint

mother_of_units = pint.UnitRegistry()

mother_of_units.load_definitions(Path(__file__).parent / "pint_currency.txt") 

บาท = บ = baht = mother_of_units.THB

# https://github.com/hgrecco/pint/blob/master/pint/default_en.txt
ถ้วย = cup  = mother_of_units.cup
# ☕ = cup
# ☕☕ = 2 * cup
# ☕☕☕ = 3 * cup
# ☕☕☕☕ = 4 * cup
# ☕☕☕☕☕ = 5 * cup

ช้อนชา = ชช = tsp = teaspoon = mother_of_units.teaspoon

ช้อนโต๊ะ = ชต  = tbsp = tablespoon = mother_of_units.tablespoon
# 🥄 = tbsp
# 🥄🥄 = 2 * tbsp
# 🥄🥄🥄 = 3 * tbsp
# 🥄🥄🥄🥄 = 4 * tbsp
# 🥄🥄🥄🥄🥄 = 5 * tbsp

g = gram = กรัม = ก = mother_of_units.gram
kg = kilogram = โล = กก = กิโลกรัม = mother_of_units.kilogram
lbs = pound = ปอนด์ = mother_of_units.pound

cal = แคล = แคลอรี่ = mother_of_units.calorie

min_ = นาที = mother_of_units.minute
hr = hour = ชั่วโมง = mother_of_units.hour