function exibirGrafico(dias) {
    console.log('Botão clicado para', dias, 'dias'); // Verifica se a função está sendo chamada

    // Use JavaScript para enviar uma requisição ao servidor com a opção selecionada
    fetch('/atualizar-grafico?dias=' + dias)
        .then(response => response.text())
        .then(grafico => {
            // Atualiza o conteúdo da div com o novo gráfico
            document.getElementById('graficoEgeon').innerHTML = grafico;
        });
}
