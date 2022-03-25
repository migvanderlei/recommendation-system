# recommendation-system


# [POST] - **/user**
- Cria um novo usuário

Exemplo de corpo da requisição
```json
{
    "username": "Fulano"
}
```
# [POST] - **/review**
- Salva o rating de um filme

Exemplo de corpo da requisição
```json
{
    "username": "Fulano",
    "movie": "Star Wars - Episode III",
    "rating": 10
}
```
# [GET] - **/movies**
- Lista todos os filmes já avaliados no sistema

# [GET] - **/recommend/\<user\>**
- Lista de recomendações para um usuário (filtrando filmes que foram avaliados pelo mesmo)
