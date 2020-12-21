using UnityEngine;
using UnityEditor;
using System.Linq;

[CustomEditor(typeof(AudioVisualizer))]
public class AudioVisualizerEditor : EditorBase
{
  AudioVisualizer vis;

  void OnEnable() => vis = (AudioVisualizer)target;

  public override void OnInspectorGUI()
  {
    #region Inspector Routine Task
    if (GUILayout.Button("Refresh Editor Layout")) EnsureStyles();
    if (centeredLabelStyle == null) EnsureStyles();

    if (vis.bandDirections.Length > AudioVisualizer.bandSize)
      vis.bandDirections = vis.bandDirections.Take(AudioVisualizer.bandSize).ToArray();

    GUILayout.Space(SpaceB);  
    #endregion

    vis.showAudioSettings = EditorGUILayout.Foldout(vis.showAudioSettings, "Audio Settings", true, foldoutStyle);
    if (vis.showAudioSettings)
    {
      GUI.enabled = false;
      EditorGUILayout.IntField("Audio Hertz", AudioVisualizer.audioHertz);
      EditorGUILayout.IntField("Sample Size", AudioVisualizer.sampleSize);
      EditorGUILayout.IntField("Band Size", AudioVisualizer.bandSize);
      GUI.enabled = true;
      GUILayout.Space(SpaceB);
    }

    vis.showMicSettings = EditorGUILayout.Foldout(vis.showMicSettings, "Mic Settings", true, foldoutStyle);
    if (vis.showMicSettings)
    {
      GUI.enabled = false;
      EditorGUILayout.TextField("Mic Device", AudioVisualizer.micDevice);
      GUI.enabled = true;
      GUILayout.Space(SpaceB);
    }

    vis.showAudioVisualizer = EditorGUILayout.Foldout(vis.showAudioVisualizer, "Audio Visualizer", true, foldoutStyle);
    if (vis.showAudioVisualizer)
    {
      EditorGUILayout.PropertyField(serializedObject.FindProperty("bandLength"), new GUIContent("Band Length"));
      EditorGUILayout.PropertyField(serializedObject.FindProperty("bandDirections"), new GUIContent("Band Directions"));
      GUILayout.Space(SpaceB);
    }

    vis.showGizmos = EditorGUILayout.Foldout(vis.showGizmos, "Gizmos", true, foldoutStyle);
    if (vis.showGizmos)
    {
      EditorGUILayout.PropertyField(serializedObject.FindProperty("bandDirGrad"), new GUIContent("Band Dir Gradient"));
      GUILayout.Space(SpaceB);
    }

    if(EditorGUI.EndChangeCheck())
    {
      // EditorApplication.QueuePlayerLoopUpdate();
      serializedObject.ApplyModifiedProperties();
      for (int b=0; b < AudioVisualizer.bandSize; b++)
        vis.bandDirections[b] = vis.bandDirections[b].normalized;
    }
  }
}