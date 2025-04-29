from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def get_product_category_pairs(
    products_df: DataFrame,
    categories_df: DataFrame,
    product_category_links_df: DataFrame
) -> DataFrame:
    products_with_categories = (
        products_df.join(
            product_category_links_df,
            products_df["product_id"] == product_category_links_df["product_id"],
            "left"
        )
        .join(
            categories_df,
            product_category_links_df["category_id"] == categories_df["category_id"],
            "left"
        )
        .select(
            products_df["product_name"],
            categories_df["category_name"]
        )
    )
    
    result_df = products_with_categories
    
    return result_df
