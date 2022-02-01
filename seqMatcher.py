from copydetect import CopyDetector

detector = CopyDetector(test_dirs=["tests"], display_t=0.5)
detector.add_file("filter.py")
detector.run()
detector.generate_html_report()

