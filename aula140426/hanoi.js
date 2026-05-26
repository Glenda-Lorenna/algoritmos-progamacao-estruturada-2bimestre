function torreDeHanoi(n, origem, destino, auxiliar, movimentos) {
    if (n === 1) {
        movimentos.push(`Mover disco 1 de ${origem} para ${destino}`);
        return;
    }

    torreDeHanoi(n - 1, origem, auxiliar, destino, movimentos);

    movimentos.push(`Mover disco ${n} de ${origem} para ${destino}`);

    torreDeHanoi(n - 1, auxiliar, destino, origem, movimentos);
}

// Programa principal
let n = 3; // você pode alterar ou usar prompt()
let movimentos = [];

torreDeHanoi(n, 'A', 'C', 'B', movimentos);

// Exibir os movimentos
movimentos.forEach((passo) => {
    console.log(passo);
}); 