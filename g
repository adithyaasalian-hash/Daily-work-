<!DOCTYPE html>
<html>
<head>
    <title>Ping Pong Ball</title>
        <style>
                body {
                                margin: 0;
                                            overflow: hidden;
                                                        background: black;
                }

                        #ball {
                                        width: 30px;
                                                    height: 30px;
                                                                background: white;
                                                                            border-radius: 50%;
                                                                                        position: absolute;
                                                                                                    top: 100px;
                                                                                                                left: 100px;
                        }
                            </style>
                            </head>

                            <body>

                            <div id="ball"></div>

                            <script>
                                let ball = document.getElementById("ball");

                                    let x = 100;
                                        let y = 100;
                                            let dx = 3;
                                                let dy = 3;

                                                    function moveBall() {
                                                                x += dx;
                                                                        y += dy;

                                                                                if (x <= 0 || x >= window.innerWidth - 30)
                                                                                            dx = -dx;

                                                                                                    if (y <= 0 || y >= window.innerHeight - 30)
                                                                                                                dy = -dy;

                                                                                                                        ball.style.left = x + "px";
                                                                                                                                ball.style.top = y + "px";

                                                                                                                                        requestAnimationFrame(moveBall);
                                                    }

                                                        moveBall();
                                                        </script>

                                                        </body>
                                                        </html>
                                                    }
                        }
                }