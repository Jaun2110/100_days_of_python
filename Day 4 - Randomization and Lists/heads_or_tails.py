import random



random_int = random.randint(0, 1)
# print(random_int)

if random_int == 1:
   print(r"""
             _.--'''-._
        .-'/         `\
       /.-'`.          '\
      '/  .-.`-. `       `
     ( }) (}\   `-._\     :
      //   .       )) '.  ;
      \`          *',     .
      /v\           /    ,'
      \_/        ' (:    .  heads
       `-.___.--'   /-.-'
            )       |
      .----'`-.___.-'`----.

   """)
else:
    print(r"""
     _        _ _ 
| |      (_) |
| |_ __ _ _| |
| __/ _` | | | tails
| || (_| | | |
 \__\__,_|_|_|
    """)
