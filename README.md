# GA-copy-image
Este simples GA tenta evoluir uma população com o objetivo de copiar uma imagem de 8-bits. Ele serve para vermos a evolução dos melhores indivíduos numa população.

Para gerar um gif com a população de imagens geradas, basta rodar a seguinte linha de comando no linux
(precisa ter o ImageMagick instalado):

~$ convert -delay 0 -loop 0 *.png -scale 400x400 space.gif

Este GA é uma versão simplificada do projeto deste cara:
https://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/
