using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.VFX;


public class RotateObject : MonoBehaviour
{
  [SerializeField]
  private float rotationSpeed = 500;
  public Vector2 rotationVelocity;
  [Range(0.8f, 0.99f)]
  public float velocityDamping = 0.9f;

  public VisualEffect audioVFX;
  public float intensityCoefficient = 0.1f;

  private float epsilon = 0.001f;

  void Start()
  {
    rotationVelocity = Vector2.zero;
  }

  void Update()
  {
    if (Input.GetMouseButton(0)) OnMouseDrag();

    if (Vector3.Dot(transform.up, Vector3.up) >= 0)
    {
      transform.Rotate(Camera.main.transform.up, -Vector3.Dot(rotationVelocity, Camera.main.transform.right), Space.World);
    } else
    {
      transform.Rotate(Camera.main.transform.up, -Vector3.Dot(rotationVelocity, Camera.main.transform.right), Space.World);
    }
    
    transform.Rotate(Camera.main.transform.right, Vector3.Dot(rotationVelocity, Camera.main.transform.up), Space.World);

    rotationVelocity *= velocityDamping;

    if (rotationVelocity.magnitude <= epsilon) rotationVelocity = Vector2.zero;

    float intensity = Mathf.Clamp(rotationVelocity.magnitude * intensityCoefficient, 0, 1);
    audioVFX.SetFloat("Intensity", intensity);
  }

  void OnMouseDrag()
  {
    float rotationX = Input.GetAxis("Mouse X")*rotationSpeed*Mathf.Deg2Rad;
    float rotationY = Input.GetAxis("Mouse Y")*rotationSpeed*Mathf.Deg2Rad;

    rotationVelocity = new Vector2(rotationX, rotationY);
  }
}
