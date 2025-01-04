# PROYECTOS
- Ejecución de modelos + Documentación (**baseGoEmotionsModel.ipynb**)
  
1. Utilizando un api de hugginface de un modelo llm crea una aplicación donde el usuario pueda realizar preguntas y el modelo le responda
 ```https://chatbotnixon0001.streamlit.app/```

3. Implemente múltiples modelos, utilizando el api cree una clase que le permite iterar de un modelo a otro, en el readme detalla con un diagrama de flujo como estas usando los modelos y da un ejemplo del resultado.

## DEFINICIÓN

### - **(baseGoEmotionsModel.ipynb)**
Para el proyecto de ejecución de modelos, se consume la libreria de transfromers de un modelo de text-classification (SamLowe/roberta-base-go_emotions), el cuál es ejecutado desde un Colab que contiene el paso a paso para su ejecución, ademas de un apartado de documentación con base a lo requerido.

### 1.Proyecto desplegado en la nube comunitaria de streamlit
URL:
```https://chatbotnixon0001.streamlit.app/```

Para este proyecto, se desarrolló una interfaz streamlit de chat con el modelo de generación de texto **Qwen2.5-Coder-32B-Instruct** por medio de la API **huggingface_hub**. 

#### **Parametros del modelo:**
```
  model="Qwen/Qwen2.5-Coder-32B-Instruct",
  messages=[
      {"role": m["role"], "content": m["content"]}
      for m in st.session_state.messages
  ],
  temperature=0.5,
  max_tokens=2048,
  top_p=0.5,
  stream=True
```
#### **Ejemplo de uso:**
La interfaz es bastante sencilla y familiar. Una vez ingresamos a la url, tendremos dos secciones, la primera será donde se muestra la pregunta y su respectiva respuesta por parte del modelo, y la segunda, es el campo de entrada de texto para hacer preguntas
![image](https://github.com/user-attachments/assets/f7308447-8cfb-4d07-bf49-9d09d29ff1aa)

Dependiendo de que tan compleja llegue a ser la pregunta, el modelo demorará más o menos tiempo. Si toma tiempo, el mensaje aparecerá como "Wait for it"
![image](https://github.com/user-attachments/assets/4e65ae78-8307-4058-bcf3-b659480a10e5)


  
