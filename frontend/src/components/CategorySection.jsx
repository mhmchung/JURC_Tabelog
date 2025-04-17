import React from "react";
import CategoryItem from "./CategoryItem";

const categories = [
  {
    id: "1",
    image: "https://images.pexels.com/photos/5417838/pexels-photo-5417838.jpeg",
    title: "Reserve",
  },
  {
    id: "2",
    image: "https://images.pexels.com/photos/31466991/pexels-photo-31466991.jpeg",
    title: "Search",
  },
  {
    id: "3",
    image: "https://images.pexels.com/photos/6193315/pexels-photo-6193315.jpeg",
    title: "Top Rated",
  },
  {
    id: "4",
    image: "https://images.pexels.com/photos/4792007/pexels-photo-4792007.jpeg",
    title: "Near Me",
  },
];

const CategorySection = () => (
  <div className="flex justify-between mb-6">
    {categories.map((category) => (
      <CategoryItem key={category.id} imageUri={category.image} title={category.title} />
    ))}
  </div>
);

export default CategorySection;
