# Run tests
odoo -c /etc/odoo/odoo.conf --test-enable -d custom_materials -i custom_materials --test-file=/mnt/extra-addons/custom_materials/tests

# Check test results
if [ $? -eq 0 ]; then
    # All tests passed, show report and start server
    echo "All tests passed. Starting server..."
    # Command to show report
    # Command to start server
else
    # Tests failed, display error message and exit
    echo "Tests failed. Server will not start."
    exit 1
fi
