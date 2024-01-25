package dto;

import lombok.Data;

import java.math.BigDecimal;

/**
 * @author wangshuai@e6yun.com
 * @date 4/8/2021 3:58 PM
 **/
@Data
public class BookDTO {
    private Integer bookId;
    private String bookName;
    private BigDecimal price;
}
