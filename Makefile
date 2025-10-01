PYTEST := pytest
TEST_DIR := tests/
ALLURE_DIR := allure_reports

.PHONY: test report clean

# Run tests and generate Allure results
test:
	@echo "Running Pytest tests..."
	@$(PYTEST) $(TEST_DIR) --alluredir=$(ALLURE_DIR) || true

# Serve Allure report (always runs, even if tests fail)
report: test
	@echo "Serving Allure report..."
	@allure serve $(ALLURE_DIR)

# Clean old Allure reports
clean:
	@echo "Cleaning Allure reports..."
	@rm -rf $(ALLURE_DIR)