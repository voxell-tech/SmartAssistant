using UnityEngine;
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

    GUILayout.Space(spaceB);  
    #endregion

    agent.showAudioSettings = EditorGUILayout.Foldout(agent.showAudioSettings, "Audio Settings", true, foldoutStyle);
    if (agent.showAudioSettings)
    {
      GUILayout.BeginVertical(box);
      EditorGUILayout.PropertyField(serializedObject.FindProperty("audioVFX"), new GUIContent("Audio VFX Graph"));
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
      // EditorApplication.QueuePlayerLoopUpdate();
      serializedObject.ApplyModifiedProperties();
    }
  }
}