using UnityEngine;
using UnityEngine.Rendering;
using UnityEditor;
using System.Linq;

[CustomEditor(typeof(Agent))]
public class AudioVisualizerEditor : EditorBase
{
  Agent agent;

  void OnEnable() => agent = (Agent)target;

  public override void OnInspectorGUI()
  {
    #region Inspector Routine Task
    if (GUILayout.Button("Refresh Editor Layout")) EnsureStyles();
    if (centeredLabelStyle == null) EnsureStyles();

    if (agent.bandDirections.Length > Agent.bandSize)
      agent.bandDirections = agent.bandDirections.Take(Agent.bandSize).ToArray();

    // if (agent.audioForceField != null && agent.textureDim == TextureDimension.None) agent.textureDim = agent.audioForceField.dimension;

    GUILayout.Space(spaceB);  
    #endregion

    agent.showAudioSettings = EditorGUILayout.Foldout(agent.showAudioSettings, "Audio Settings", true, foldoutStyle);
    if (agent.showAudioSettings)
    {
      GUILayout.BeginVertical(box);
      EditorGUILayout.PropertyField(serializedObject.FindProperty("audioVFX"), new GUIContent("Audio VFX Graph"));
      EditorGUILayout.PropertyField(serializedObject.FindProperty("audioSource"), new GUIContent("Audio Source"));
      EditorGUILayout.PropertyField(serializedObject.FindProperty("fft"), new GUIContent("FFT Window"));
      GUI.enabled = false;
      EditorGUILayout.IntField("Audio Hertz", Agent.audioHertz);
      EditorGUILayout.IntField("Sample Size", Agent.sampleSize);
      EditorGUILayout.IntField("Band Size", Agent.bandSize);
      GUI.enabled = true;
      GUILayout.EndVertical();
      GUILayout.Space(spaceA);
    }

    agent.showMicSettings = EditorGUILayout.Foldout(agent.showMicSettings, "Mic Settings", true, foldoutStyle);
    if (agent.showMicSettings)
    {
      GUILayout.BeginVertical(box);
      GUI.enabled = false;
      EditorGUILayout.TextField("Mic Device", Agent.micDevice);
      GUI.enabled = true;
      GUILayout.EndVertical();
      GUILayout.Space(spaceA);
    }

    agent.showAudioVisualizer = EditorGUILayout.Foldout(agent.showAudioVisualizer, "Audio Visualizer", true, foldoutStyle);
    if (agent.showAudioVisualizer)
    {
      GUILayout.BeginVertical(box);
      EditorGUILayout.PropertyField(serializedObject.FindProperty("bandLength"), new GUIContent("Band Length"));
      EditorGUILayout.PropertyField(serializedObject.FindProperty("bandDirections"), new GUIContent("Band Directions"));
      EditorGUILayout.PropertyField(serializedObject.FindProperty("bandDirGrad"), new GUIContent("Band Dir Gradient"));

      // EditorGUILayout.PropertyField(serializedObject.FindProperty("audioForceField"), new GUIContent("Audio Force Field"));
      // GUI.enabled = false;
      // EditorGUILayout.PropertyField(serializedObject.FindProperty("textureDim"), new GUIContent("Force Field Dimension"));
      // GUI.enabled = true;
      GUILayout.Space(spaceB);
      
      if (GUILayout.Button("Normalize Directions"))
      {
        for (int b=0; b < Agent.bandSize; b++)
          agent.bandDirections[b] = agent.bandDirections[b].normalized;
      }
      GUILayout.EndVertical();
      GUILayout.Space(spaceA);
    }

    agent.showAgentInteraction = EditorGUILayout.Foldout(agent.showAgentInteraction, "Agent Interaction", true, foldoutStyle);
    if (agent.showAgentInteraction)
    {
      GUILayout.BeginVertical(box);
      agent.showRotation = EditorGUILayout.Foldout(agent.showRotation, "Rotatation", true, subFoldoutStyle);
      if (agent.showRotation)
      {
        EditorGUILayout.PropertyField(serializedObject.FindProperty("rotationMultiplier"), new GUIContent("Rotation Multiplier"));
        EditorGUILayout.PropertyField(serializedObject.FindProperty("velocityDamping"), new GUIContent("Velocity Damping"));
        EditorGUILayout.PropertyField(serializedObject.FindProperty("intensityCoefficient"), new GUIContent("Intensity Coefficient"));
        EditorGUILayout.PropertyField(serializedObject.FindProperty("intervalTime"), new GUIContent("Interval Update Time"));
        GUI.enabled = false;
        EditorGUILayout.PropertyField(serializedObject.FindProperty("rotationVelocity"), new GUIContent("Rotation Velocity"));
        GUI.enabled = true;
        GUILayout.Space(spaceB);
      }

      GUILayout.EndVertical();
      GUILayout.Space(spaceA);
    }

    if(EditorGUI.EndChangeCheck())
    {
      EditorApplication.QueuePlayerLoopUpdate();
      serializedObject.ApplyModifiedProperties();
    }

    agent.drawDefaultInspect = EditorGUILayout.Foldout(agent.drawDefaultInspect, "Draw Default Inspector", true, foldoutStyle);
    if (agent.drawDefaultInspect)
      DrawDefaultInspector();
  }
}