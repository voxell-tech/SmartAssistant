using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.VFX;

[RequireComponent(typeof(VisualEffect))]
[RequireComponent(typeof(AudioSource))]
public partial class Agent : MonoBehaviour
{
  void Start()
  {
    InitAgentInteraction();
    InitAudioVisualizer();
  }

  void Update()
  {
    UpdateAgentInteraction();
    UpdateAudioVisualizer();
  }
}
