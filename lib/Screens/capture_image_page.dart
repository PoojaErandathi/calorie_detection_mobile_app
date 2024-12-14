import 'package:flutter/material.dart';
import 'package:camera/camera.dart';

class CaptureImagePage extends StatefulWidget {
  @override
  _CaptureImagePageState createState() => _CaptureImagePageState();
}

class _CaptureImagePageState extends State<CaptureImagePage> {
  CameraController? _controller;
  Future<void>? _initializeControllerFuture;

  // Flag to check if camera is initialized
  bool _isCameraInitialized = false;

  void _initializeCamera() async {
    try {
      final cameras = await availableCameras();
      final firstCamera = cameras.first;

      _controller = CameraController(firstCamera, ResolutionPreset.medium);
      _initializeControllerFuture = _controller?.initialize();

      await _initializeControllerFuture; // Wait for camera initialization

      setState(() {
        _isCameraInitialized = true;
      });
    } catch (e) {
      print("Error initializing camera: $e");
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Failed to open camera: $e')),
      );
    }
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Capture Image'),
      ),
      body: _isCameraInitialized && _controller != null
          ? FutureBuilder<void>(
              future: _initializeControllerFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  return CameraPreview(_controller!);
                } else {
                  return const Center(child: CircularProgressIndicator());
                }
              },
            )
          : const Center(
              child: Text(
                'Press the camera button to start the camera',
                style: TextStyle(fontSize: 16, color: Colors.grey),
              ),
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          if (!_isCameraInitialized) {
            _initializeCamera();
          } else {
            _captureImage();
          }
        },
        child: const Icon(Icons.camera_alt),
      ),
    );
  }

  Future<void> _captureImage() async {
    try {
      if (_controller != null) {
        final image = await _controller!.takePicture();
        if (image != null) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text('Image saved at ${image.path}')),
          );
        }
      }
    } catch (e) {
      print("Error capturing image: $e");
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Failed to capture image: $e')),
      );
    }
  }
}
