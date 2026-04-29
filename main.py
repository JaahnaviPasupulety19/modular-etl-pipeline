# import pandas as pd
# import yaml

# # Clean imports using __init__.py
# from pipeline import (
#     handle_missing,
#     remove_duplicates,
#     scale_data,
#     validate_columns
# )

# from utils.logger import get_logger

# logger = get_logger()

# def run_pipeline(config_path="config/config.yaml"):
#     try:
#         # Load config
#         with open(config_path, "r") as f:
#             config = yaml.safe_load(f)

#         logger.info("Config loaded successfully")

#         # Load dataset
#         df = pd.read_csv(config["dataset"])
#         logger.info(f"Dataset loaded: {config['dataset']}")

#         # Validation
#         validate_columns(df, config["required_columns"])
#         logger.info("Validation passed")

#         # Cleaning
#         df = handle_missing(df)
#         df = remove_duplicates(df)
#         logger.info("Cleaning completed")

#         # Transformation
#         columns = config.get("columns_to_scale", None)
#         df = scale_data(df, columns)
#         logger.info("Transformation completed")

#         # Save output (IMPORTANT 🔥)
#         output_path = config.get("output_path", "data/output.csv")
#         df.to_csv(output_path, index=False)

#         logger.info(f"Processed data saved to: {output_path}")

#         print("✅ Pipeline executed successfully")

#     except Exception as e:
#         logger.error(f"❌ Error occurred: {str(e)}")
#         print("Pipeline failed. Check logs.")

# # Run pipeline
# if __name__ == "__main__":
#     run_pipeline("config/netflix.yaml")




# #   To Run file:
# #     >pip install -r requirements.txt
# #     >python main.py
# #     >python main.py --config config/netflix.yaml



import pandas as pd
import yaml
import argparse

from pipeline import (
    handle_missing,
    remove_duplicates,
    scale_data,
    validate_columns,
    validate_nulls   # 👈 ADD THIS
)

from utils.logger import get_logger

logger = get_logger()


def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def run_pipeline(config):
    try:
        # Load dataset
        df = pd.read_csv(config["dataset"])
        logger.info(f"Dataset loaded: {config['dataset']}")

        # Validation (only column check here)
        validate_columns(df, config.get("required_columns", []))
        logger.info("Column validation passed")

        # Cleaning
        df = handle_missing(df)
        df = remove_duplicates(df)
        logger.info("Cleaning completed")

        # Validate nulls AFTER cleaning
        validate_nulls(df, config.get("required_columns", []))
        logger.info("Null validation passed")

  

        # Transformation
        df = scale_data(df, config.get("columns_to_scale"))
        logger.info("Transformation completed")

        # Save output
        output_path = config.get("output_path", "data/output.csv")
        df.to_csv(output_path, index=False)

        logger.info(f"Processed data saved to: {output_path}")
        print("✅ Pipeline executed successfully")

    except Exception as e:
        logger.exception("Pipeline failed")
        print("❌ Pipeline failed. Check logs.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ETL Pipeline")
    parser.add_argument(
        "--config",
        type=str,
        default="config/config.yaml",
        help="Path to config file"
    )

    args = parser.parse_args()

    config = load_config(args.config)
    logger.info("Config loaded successfully")

    run_pipeline(config)