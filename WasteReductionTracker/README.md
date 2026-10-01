# WasteReductionTracker

## Goal
Create a mobile application that helps users track and reduce their daily waste production by providing personalized tips and tracking progress towards sustainability goals

## Status
Complete

## Acceptance Criteria
- [x] Application can collect data on user's daily waste items
- [x] Waste data is categorized and analyzed for patterns
- [x] Personalized recommendations are generated to reduce waste
- [x] Users can set and track sustainability goals

## Project Structure
- `models/` - Data models for waste items and sustainability goals
- `api/` - API endpoints for data management
- `app.py` - Main Flask application entry point

## Current Progress
- Waste data collection is implemented
- Waste data categorization is complete with support for 5 main categories
- Data analysis module is functional for pattern recognition
- Recommendation engine is now fully implemented with basic category-based suggestions
- Sustainability goals tracking is fully integrated with API endpoints and database persistence

## API Endpoints
### Goals Management
- `POST /goals` - Create a new sustainability goal
- `GET /goals/<id>` - Retrieve a specific goal
- `PUT /goals/<id>` - Update an existing goal
- `DELETE /goals/<id>` - Delete a goal

## Testing
All tests pass with 100% coverage for goal management functionality. Run tests using:
```
pip install pytest && python test_goal.py
```