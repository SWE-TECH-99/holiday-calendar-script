# Holiday Calendar Script

Generate custom holiday calendar files (.ics) that can be imported into popular calendar applications like Google Calendar, Apple Calendar, and Microsoft Outlook.

## Overview

This Python script helps you maintain your work holiday schedule by generating a standardized calendar file that:

- Creates full-day and half-day holiday events
- Automatically excludes weekends and standard holidays
- Supports flexible date ranges and custom descriptions
- Exports in the universal .ics format for maximum compatibility

## Requirements

- Python 3.6+
- `ics` package

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/SWE-TECH-99/holiday-calendar-script.git
   cd holiday-calendar-script
   ```

2. Install dependencies:
   ```bash
   pip install ics
   ```

3. Run the script:
   ```bash
   python generate_calendar.py
   ```

4. Import the generated `Holidays_From_Work.ics` file into your calendar application.

## Calendar Application Import Guide

### Google Calendar
1. Open [Google Calendar](https://calendar.google.com)
2. Click the gear icon (Settings)
3. Select "Import & export"
4. Click "Select file from your computer"
5. Choose your .ics file
6. Select the destination calendar
7. Click "Import"

### Apple Calendar
1. Open Calendar app
2. File → Import
3. Select your .ics file
4. Choose which calendar to add events to
5. Click "Import"

### Microsoft Outlook
1. Open Outlook
2. File → Open & Export → Import/Export
3. Select "Import an iCalendar (.ics) file"
4. Browse to your .ics file
5. Click "Import"

## Customization

### Adding Holiday Events

Modify the `holidays` list in the script to set your schedule:

```python
holidays = [
    {
        "date": "2024-12-20",
        "description": "Full Day"
    },
    {
        "date": "2024-12-23",
        "description": "Half Day (AM)"
    },
    {
        "date": "2024-12-31",
        "description": "Half Day (PM)"
    }
]
```

### Event Types

The script supports three types of holiday events:
- Full Day: Takes up the entire working day
- Half Day (AM): Morning holiday (usually ends at lunch)
- Half Day (PM): Afternoon holiday (usually starts at lunch)

### Excluded Dates

By default, the script excludes:
- Weekends (Saturday and Sunday)
- Major holidays:
  - New Year's Day (January 1)
  - Christmas Day (December 25)
  - Boxing Day (December 26)

To modify these exclusions, edit the `EXCLUDED_DATES` list in the script.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Maintain backward compatibility

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

1. **Import Fails**: Ensure your calendar application supports .ics version 2.0
2. **Script Error**: Verify Python 3.6+ is installed and the ics package is up to date
3. **Missing Events**: Check if dates fall on excluded days (weekends/holidays)

### Getting Help

- Open an issue on GitHub
- Check existing issues for solutions
- Include error messages and OS details when reporting problems

## Version History

- 1.0.0 (2024-03-15): Initial release
- 1.0.1 (2024-03-20): Added half-day support
- 1.1.0 (2024-04-01): Added custom exclusion dates

## Acknowledgments

- [ics-py](https://github.com/ics-py/ics-py) for the calendar generation library
- Contributors who have helped improve the script

## Contact

Project Link: [https://github.com/SWE-TECH-99/holiday-calendar-script](https://github.com/SWE-TECH-99/holiday-calendar-script)
