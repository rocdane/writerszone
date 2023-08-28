# writerszone
Writers Zone (Site web d'informations et d'actualités) [info](https://github.com/rocdane/writerszone)

## Description
Writers Zone est un projet qui vise la liberté d'expression. Ce projet est composé de blog, de réseau social et de chat.

## Public
Ce projet peut servir de plateforme de libre échange entre internaute.

## Fonctionnalités
1. En tant que Utilisateur je crée un compte utilisateur
2. En tant que Utilisateur je mets à jour mon profile
3. En tant que Utilisateur, je publie un article sur le blog
4. En tant que Utilisateur, je télécharge un article du blog
5. En tant que Utilisateur, je publie un post sur le réseau social
6. En tant que Utilisateur, je note un post sur le réseau social
7. En tant que Utilisateur, je commente un post sur le réseau social
8. En tant que Utilisateur, je chatte avec un autre utilisateur

## Concepts

```json
{
	"user":{
		"username":"string",
		"password":"string|crypto",
		"role":["admin","superuser"]
	},
	"profile":{
		"name":"string",
		"legacy":"string",
		"email":"string",
		"phone":"string",
		"address":"string",
		"owner":"user",
		"followers":["profile"]
	},
	"article":{
		"title":"string",
		"resume":"text",
		"content":"text",
		"views":"integer",
		"likes":"integer",
		"created_at":"timestamp",
		"updated_at":"timestamp",
		"author":"profile"
	},
	"post":{
		"content":"string",
		"media":"bytes",
		"views":"integer",
		"likes":"integer",
		"created_at":"timestamp",
		"updated_at":"timestamp",
		"author":"profile"
	},
	"comment":{
		"message":"string",
		"likes":"integer",
		"unlikes":"integer",
		"created_at":"timestamp",
		"updated_at":"timestamp",
		"author":"profile",
		"owner":"post"
	},
	"chat":{
		"message":"string",
		"media":"bytes",
		"sender":"profile",
		"receiver":"profile",
		"sended_at":"timestamp",
		"readed_at":"timestamp"
	}
}
```
