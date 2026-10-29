class PersonajeGenshin:
    def __init__(self, nombre, elemento):
        self.nombre = nombre
        self.elemento = elemento
        self.energia = 0  # El personaje siempre empieza con 0 de energía

    def usar_habilidad_basica(self):
        # Cada vez que ataca, suma 50 de energía
        self.energia += 50
        print(f"⚔️ {self.nombre} ataca con {self.elemento}. Energía actual: {self.energia}/100")

    def lanzar_definitiva(self):
        # Evaluamos si tiene la energía al máximo (100) para lanzar el poder
        if self.energia >= 100:
            print(f"🌟 ¡{self.nombre} desata su explosión definitiva {self.elemento}!")
            self.energia = 0  # Se gasta toda la energía tras usarla
        else:
            print(f"⚠️ A {self.nombre} le falta energía ({self.energia}/100) para su definitiva.")

# 1. Creamos al personaje
kinich = PersonajeGenshin("Kinich", "Dendro")

# 2. Intentamos usar la definitiva sin energía
kinich.lanzar_definitiva()

# 3. Usamos la habilidad básica un par de veces para cargarla
kinich.usar_habilidad_basica()
kinich.usar_habilidad_basica()

# 4. Ahora sí, lanzamos la definitiva
kinich.lanzar_definitiva()