# pygame-brownian-ball

This is a simple app that simulates Brownian Ball, that bounces in randome directions inside a box, made with pygame

## Program output
![](https://github.com/dtymkiv/pygame-brownian-ball/blob/main/readme.d/animation.gif)


## Notes
Since we used to imagine axis directions as follows
![](https://github.com/dtymkiv/pygame-brownian-ball/blob/main/readme.d/circle.png)

But pygame's axis looks like this
![](https://github.com/dtymkiv/pygame-brownian-ball/blob/main/readme.d/axis.png)

Therefore, some adjustments were made on how ball bounces:

- bottom bounce: random direcrion from 90 to 270 degrees
- left bounce: random direcrion from 0 to 180 degrees
- top bounce: random direcrion from 270 to 90 degrees
- right bounce: random direcrion from 180 to 360 degrees