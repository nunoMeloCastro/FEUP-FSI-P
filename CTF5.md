# CTF realizado na Semana #5

## Desafio 1

### Existe algum ficheiro que é aberto e lido pelo programa?
Sim, o programa abre e lê o ficheiro que é passado à variável meme_file.

### Existe alguma forma de controlar o ficheiro que é aberto?
É possível controlar este ficheiro dando overwrite ao conteúdo da variável meme_file.

### Existe algum buffer-overflow? Se sim, o que é que podes fazer?
Existe. A vulnerabilidade está no programa criar dois buffers, um de tamanho 20 e outro de 8, e no scanf ser permitido escrever 28 bytes. Deste modo é possível escrever por cima do buffer e também dar overwrite do ficheiro passado no meme_file, desde que este tenha nome de comprimento inferior ou igual a 8 bytes.

![image-4.png](./image-4.png)

O ataque consisitiu então em enviar 20 caratéres aleatórios seguidos do nome do ficheiro pretendido, neste caso flag.txt. 
Ao fazer isto é dado então overwrite da variável meme_file que de seguida é consumido pelo fopen() para ler o ficheiro que é printado para o stdout, sendo a flag do desafio.

![image-6.png](./image-6.png)
![image-7.png](./image-7.png)

## Desafio 2

### Que alterações foram feitas?
Foi adicionada a leitura de uma variável de controlo de 4 bytes. 

### Mitigam na totalidade o problema?
Não necessariamente pois é possível reescrever estes 4 bytes para o valor desejado de modo a obter a flag.
O valor de controlo pretendido é 0xfefc2122 mas apenas temos 4 bytes de input para ele. Porém é possível passar bytes em hexadecimal no stdin através de "\x".

### É possivel ultrapassar a mitigação usando uma técnica similar à que foi utilizada anteriormente?
Sim, é possível pois o scanf permite escrever 32 bytes, logo ao dar 20 bytes aleatórios seguido dos 4 bytes da variável de controlo de forma a entrar de novo no fopen e os restantes 8 bytes com o nome do ficheiro que se pretende abrir. totalizando assim nos 32 bytes necessários.

![image-8.png](./image-8.png)
![image-9.png](./image-9.png)
![image-10.png](./image-10.png)

