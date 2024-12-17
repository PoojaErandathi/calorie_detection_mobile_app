
import 'package:calorie_detection_mobile_app/Screens/capture_image_page.dart';
import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  Widget _buildSquareButton(String title, IconData icon, VoidCallback onPressed) {
    return ElevatedButton(
      onPressed: onPressed,
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.blueAccent,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
        padding: EdgeInsets.zero, // Ensures square shape
      ),
      child: Container(
        width: 120,
        height: 120,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, size: 40, color: Colors.white),
            const SizedBox(height: 8),
            Text(
              title,
              style: const TextStyle(fontSize: 16, color: Colors.white),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home Page'),
      ),
      body: SingleChildScrollView(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Image at the Top
              Padding(
                padding: const EdgeInsets.only(top: 20.0, bottom: 20.0),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(16),
                  child: Image.asset(
                    'assets/images/home_page.jpg', // Replace with your image file name
                    width: 300,
                    height: 200,
                    fit: BoxFit.cover,
                    errorBuilder: (context, error, stackTrace) {
                      return const Center(
                        child: Text(
                          'Image not found',
                          style: TextStyle(fontSize: 16, color: Colors.red),
                        ),
                      );
                    },
                  ),
                ),
              ),
              // First Row of Buttons
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildSquareButton(
                    "Calorie Calculator",
                    Icons.calculate,
                    () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => CaptureImagePage()),
                      );
                    },
                  ),
                  _buildSquareButton(
                    "Calorie History",
                    Icons.bar_chart,
                    () {
                      Navigator.pushNamed(context, '/calorie_history');
                    },
                  ),
                ],
              ),
              const SizedBox(height: 20), // Spacing between rows
              // Second Row of Buttons
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildSquareButton(
                    "Calorie Meter",
                    Icons.search,
                    () {
                      Navigator.pushNamed(context, '/calorie_meter');
                    },
                  ),
                  _buildSquareButton(
                    "Healthy Food Tips",
                    Icons.health_and_safety,
                    () {
                      Navigator.pushNamed(context, '/healthy_food_tips');
                    },
                  ),
                ],
              ),
              const SizedBox(height: 30), // Extra spacing at the bottom
            ],
          ),
        ),
      ),

    );
  }
}
