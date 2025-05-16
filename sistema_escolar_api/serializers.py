from rest_framework import serializers
from rest_framework.authtoken.models import Token
from sistema_escolar_api.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

class AdminSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Administradores
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Alumnos
        fields = "__all__"

class MaestroSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Maestros
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data_copy = data.copy()
        if 'hora_inicio' in data_copy:
            data_copy['horaInicio'] = data_copy.pop('hora_inicio')
        if 'hora_fin' in data_copy:
            data_copy['horaFin'] = data_copy.pop('hora_fin')
        if 'cupo_asistentes' in data_copy:
            data_copy['cupoAsistentes'] = data_copy.pop('cupo_asistentes')
        if 'programa_educativo' in data_copy:
            data_copy['programaEducativo'] = data_copy.pop('programa_educativo')
        # Si 'publico_objetivo' viene como arreglo, lo convertimos a cadena separada por comas.
        if 'publico_objetivo' in data_copy and isinstance(data_copy['publico_objetivo'], list):
            data_copy['publico_objetivo'] = ','.join(data_copy['publico_objetivo'])
        # Convertir responsable a cadena (si es numérico)
        if 'responsable' in data_copy:
            data_copy['responsable'] = str(data_copy['responsable'])
        return super().to_internal_value(data_copy)
    
    class Meta:
        model = Evento
        fields = ('id', 'nombre', 'tipo', 'fecha_realizacion', 'horaInicio', 'horaFin', 'lugar',
                  'descripcion', 'cupoAsistentes', 'programaEducativo', 'publico_objetivo', 'responsable')