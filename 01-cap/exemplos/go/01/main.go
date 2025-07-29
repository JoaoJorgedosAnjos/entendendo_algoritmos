package main

import "fmt"

func main() {
	minha_lista := []int{1,3,5,7,9}

	fmt.Println(pesquisa_binaria(minha_lista, 7))
}

func pesquisa_binaria(lista []int, item int) int {
	baixo := 0
	alto := len(lista) - 1

	for baixo <= alto {
		meio := (baixo + alto) / 2
		chute := lista[meio]

		if chute == item {
			return meio
		}
		if chute > item {
			alto = meio - 1
		}
		if chute < item {
			baixo = meio + 1
		}
	}
	return -1
}
