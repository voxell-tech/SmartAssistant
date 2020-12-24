using UnityEngine;
using UnityEngine.VFX;

public partial class Agent : MonoBehaviour
{
  #region Audio Settings
  private const float epsilon = 0.001f;
  public AudioSource audioSource;
  public AudioClip audioClip;
  public FFTWindow fft;

  public const int audioHertz = 44100;
  public const int sampleSize = 512;
  public static float[] spectrumLeft;
  public static float[] spectrumRight;

  public const int bandSize = 8;
  public float[] bandLeft;
  public static float[] bandRight;
  #endregion

  #region Mic Settings
  public static string micDevice;
  #endregion

  #region Audio Visualizer
  public float bandLength = 5.0f;
  public Vector3[] bandDirections = new Vector3[bandSize];
  public Vector3[] bandPoints = new Vector3[bandSize];
  public Gradient bandDirGrad;
  #endregion

  #region Editor Stuffs
  public bool showAudioSettings,
  showMicSettings,
  showAudioVisualizer;
  #endregion
  
  void InitAudioVisualizer()
  {
    print(sampleSize);
    spectrumLeft = new float[sampleSize];
    spectrumRight = new float[sampleSize];
    bandLeft = new float[bandSize];
    bandRight = new float[bandSize];

    micDevice = Microphone.devices[0].ToString();

    audioSource.Play();
    SetVFXAudioForcePositions();
    SetBandPoints();
  }

  void UpdateAudioVisualizer()
  {
    audioSource.GetSpectrumData(spectrumLeft, 0, fft);
    audioSource.GetSpectrumData(spectrumRight, 1, fft);

    CreateFreqBand(ref bandLeft, ref spectrumLeft);
    CreateFreqBand(ref bandRight, ref spectrumRight);
    UpdateVFXAudioForcePositions();
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

  public void SetBandPoints()
  {
    for (int b=0; b < bandSize; b++) bandPoints[b] = transform.position + bandDirections[b]*bandLength;
  }

  void SetVFXAudioForcePositions()
  {
    audioVFX.SetVector4(audio1, bandPoints[0]);
    audioVFX.SetVector4(audio2, bandPoints[1]);
    audioVFX.SetVector4(audio3, bandPoints[2]);
    audioVFX.SetVector4(audio4, bandPoints[3]);
    audioVFX.SetVector4(audio5, bandPoints[4]);
    audioVFX.SetVector4(audio6, bandPoints[5]);
    audioVFX.SetVector4(audio7, bandPoints[6]);
    audioVFX.SetVector4(audio8, bandPoints[7]);
  }

  void UpdateVFXAudioForcePositions()
  {
    audioVFX.SetVector4(audio1, SetForce(bandPoints[0], ref bandLeft[0]));
    audioVFX.SetVector4(audio2, SetForce(bandPoints[1], ref bandLeft[1]));
    audioVFX.SetVector4(audio3, SetForce(bandPoints[2], ref bandLeft[2]));
    audioVFX.SetVector4(audio4, SetForce(bandPoints[3], ref bandLeft[3]));
    audioVFX.SetVector4(audio5, SetForce(bandPoints[4], ref bandLeft[4]));
    audioVFX.SetVector4(audio6, SetForce(bandPoints[5], ref bandLeft[5]));
    audioVFX.SetVector4(audio7, SetForce(bandPoints[6], ref bandLeft[6]));
    audioVFX.SetVector4(audio8, SetForce(bandPoints[7], ref bandLeft[7]));
  }

  Vector4 SetForce(Vector3 position, ref float force)
  {
    return new Vector4(position.x, position.y, position.z, Mathf.Clamp(force, 0, 1));
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
