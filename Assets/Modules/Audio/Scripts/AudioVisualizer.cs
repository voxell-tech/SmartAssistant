using UnityEngine;
using UnityEngine.VFX;

public partial class Agent : MonoBehaviour
{
  #region Audio Settings
  public VisualEffect audioVFX;
  private const float epsilon = 0.001f;
  public AudioSource audioSource;
  public AudioClip audioClip;
  public FFTWindow fft;

  public const int audioHertz = 44100;
  public const int sampleSize = 1024;
  public static float[] spectrumLeft;
  public static float[] spectrumRight;

  public const int bandSize = 8;
  public static float[] bandLeft;
  public static float[] bandRight;
  #endregion

  #region Mic Settings
  public static string micDevice;
  #endregion

  #region Audio Visualizer
  public float bandLength = 5.0f;
  public Vector3[] bandDirections = new Vector3[bandSize];
  public Gradient bandDirGrad;
  #endregion

  #region Editor Stuffs
  public bool showAudioSettings,
  showMicSettings,
  showAudioVisualizer;
  #endregion
  
  void InitAudioVisualizer()
  {
    spectrumLeft = new float[sampleSize];
    spectrumRight = new float[sampleSize];
    bandLeft = new float[bandSize];
    bandRight = new float[bandSize];

    micDevice = Microphone.devices[0].ToString();


    audioSource.Play();
  }

  void UpdateAudioVisualizer()
  {
    audioSource.GetSpectrumData(spectrumLeft, 0, fft);
    audioSource.GetSpectrumData(spectrumRight, 1, fft);

    CreateFreqBand(ref bandLeft, ref spectrumLeft);
    CreateFreqBand(ref bandRight, ref spectrumRight);
  }

  void CreateFreqBand(ref float[] band, ref float[] spectrum)
  {
    int count = 0;

    for (int i=0; i < bandSize; i++)
    {
      int sampleCount = (int) Mathf.Pow(2, i) * 2;
      if (i == 7) sampleCount += 2;

      float average = 0;
      for (int s=0; s < sampleCount; s++)
      {
        average += spectrum[count]*(count + 1);
        count ++;
      }

      average /= count;
      band[i] = average * 10;
    }
  }

  void OnDrawGizmos()
  {
    for (int b=0; b < bandSize; b++)
    {
      Gizmos.color = bandDirGrad.Evaluate(b/(float) bandSize);
      Gizmos.DrawLine(transform.position, transform.position + bandDirections[b]*bandLength);
      Gizmos.DrawSphere(transform.position + bandDirections[b]*bandLength, 0.01f);
    }

    for (int b=0; b < bandSize; b++)
    {
      Gizmos.color = bandDirGrad.Evaluate(b/(float) bandSize);
      Gizmos.DrawLine(transform.position, transform.position + new Vector3(
        -bandDirections[b].x*bandLength,
        bandDirections[b].y*bandLength,
        bandDirections[b].z*bandLength));
      Gizmos.DrawSphere(transform.position + new Vector3(
        -bandDirections[b].x*bandLength,
        bandDirections[b].y*bandLength,
        bandDirections[b].z*bandLength), 0.01f);
    }
  }
}
