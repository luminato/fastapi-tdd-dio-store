from typing import List
from uuid import UUID
import pytest
from store.usecases.product import product_usecase
from store.schemas.product import ProductOut, ProductUpdateOut
from store.core.exceptions import NotFoundException


@pytest.mark.asyncio
async def test_usecases_create_should_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"


@pytest.mark.asyncio
async def test_usecases_get_should_sucess(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"


@pytest.mark.asyncio
async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("123e4567-e89b-12d3-a456-426655440000"))

    assert (
        err.value.message
        == "Product not found with filter: 123e4567-e89b-12d3-a456-426655440000"
    )


@pytest.mark.asyncio
@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_sucess():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


@pytest.mark.asyncio
async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = "7.500"
    result = await product_usecase.update(
        id=UUID("f81d907b-b150-449f-8942-77ab83d10c1d"), body=product_up
    )

    assert isinstance(result, ProductUpdateOut)


@pytest.mark.asyncio
async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(
        id=UUID("f81d907b-b150-449f-8942-77ab83d10c1d")
    )

    assert result is True


@pytest.mark.asyncio
async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )
