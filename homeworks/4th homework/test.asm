# test.asm

# Первый вектор

LOAD_CONST 200 #Value 200 - Add 210
WRITE_MEM 10 0

LOAD_CONST 222 #Value 222 - Add 224
WRITE_MEM 2 0

LOAD_CONST 225 #Value 225 - Add 227
WRITE_MEM 2 0

LOAD_CONST 160 #Value 160 - Add 162
WRITE_MEM 2 0

LOAD_CONST 190 #Value 190 - Add 193
WRITE_MEM 3 0

LOAD_CONST 195 #Value 195 - Add 198
WRITE_MEM 3 0

LOAD_CONST 130 #Value 130 - Add 133
WRITE_MEM 3 0

#Второй вектор

LOAD_CONST 240 #Value 240 - Add 242
WRITE_MEM 2 0

LOAD_CONST 221 #Value 221 - Add 225
WRITE_MEM 4 0

LOAD_CONST 230 #Value 230 - Add 232
WRITE_MEM 2 0

LOAD_CONST 160 #Value 160 - Add 165
WRITE_MEM 5 0

LOAD_CONST 190 #Value 190 - Add 194
WRITE_MEM 4 0

LOAD_CONST 195 #Value 195 - Add 199
WRITE_MEM 4 0

LOAD_CONST 200 #Value 100 - Add 202
WRITE_MEM 2 0

#Считывание
READ_MEM 210 0
READ_MEM 224 0
READ_MEM 227 0
READ_MEM 162 0
READ_MEM 193 0
READ_MEM 198 0
READ_MEM 133 0

#Сравнение
EQUAL 72 0 # Сравнение 130 и 200
WRITE_MEM 200 0

EQUAL 4 0 # Сравнение 195 и 195
WRITE_MEM 203 0

EQUAL 4 0 # Сравнение 190 и 190
WRITE_MEM 206 0

EQUAL 5 0 # Сравнение 160 и 160
WRITE_MEM 208 0

EQUAL 7 0 # Сравнение 225 и 230
WRITE_MEM 210 0

EQUAL 3 0 # Сравнение 222 и 221
WRITE_MEM 212 0

EQUAL 42 0 # Сравнение 200 и 240
WRITE_MEM 214 0